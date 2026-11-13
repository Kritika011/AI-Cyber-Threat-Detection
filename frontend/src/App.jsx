
import { useEffect, useState } from "react";
import "./App.css";

const API = "http://localhost:8000";

function App() {
  const [history, setHistory] = useState([]);
  const [page, setPage] = useState("Overview");
  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [selectedDetection, setSelectedDetection] = useState(null);

  // Load detection history from FastAPI
  async function loadHistory() {
    setLoading(true);

    try {
      const response = await fetch(`${API}/history?limit=100`);

      if (!response.ok) {
        throw new Error("Could not load history");
      }

      const data = await response.json();
      setHistory(data.history || []);
    } catch (error) {
      setMessage(
        "Cannot connect to FastAPI. Check that the backend is running."
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadHistory();
  }, []);

  // Navigate between dashboard pages
  function navigateTo(nextPage) {
    setSelectedDetection(null);
    setPage(nextPage);
    setMessage("");
  }

  // Open individual threat details
  function openDetection(item) {
    setSelectedDetection(item);
  }

  // Close details and return to the previous page
  function closeDetection() {
    setSelectedDetection(null);
  }

  // Upload CSV file for prediction
  async function uploadCSV() {
    if (!selectedFile) {
      setMessage("Please select a CSV file first.");
      return;
    }

    setUploading(true);
    setMessage("");

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch(`${API}/predict`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Prediction failed");
      }

      setMessage(
        `Success! ${data.saved_count} flows analysed and saved to MongoDB.`
      );

      setSelectedFile(null);

      const fileInput = document.getElementById("csv-upload");
      if (fileInput) {
        fileInput.value = "";
      }

      await loadHistory();
      setPage("History");
      setSelectedDetection(null);
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    } finally {
      setUploading(false);
    }
  }

  // Dashboard statistics
  const total = history.length;

  const attacks = history.filter(
    (item) => item.prediction !== "BENIGN"
  );

  const benign = history.filter(
    (item) => item.prediction === "BENIGN"
  );

  const highRisk = history.filter(
    (item) =>
      item.risk_level === "High" ||
      item.risk_level === "Critical"
  );

  // Attack distribution
  const attackTypes = {};

  attacks.forEach((item) => {
    attackTypes[item.prediction] =
      (attackTypes[item.prediction] || 0) + 1;
  });

  const sortedAttacks = Object.entries(attackTypes).sort(
    (a, b) => b[1] - a[1]
  );

  return (
    <div className="app-shell">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">⌁</div>

          <div>
            <h2>CyberSentinel</h2>
            <span>AI THREAT INTELLIGENCE</span>
          </div>
        </div>

        <div className="nav-label">WORKSPACE</div>

        {["Overview", "Threat Detection", "History"].map(
          (item, index) => (
            <button
              key={item}
              className={`nav-item ${
                page === item && !selectedDetection ? "active" : ""
              }`}
              onClick={() => navigateTo(item)}
            >
              <span>{["▦", "⌕", "◷"][index]}</span>
              {item}
            </button>
          )
        )}

        <div className="sidebar-bottom">
          <div className="connection">
            <span className="status-dot"></span>

            <div>
              <strong>System Status</strong>
              <small>FastAPI connection configured</small>
            </div>
          </div>

          <p>AI Cyber Threat Detection</p>
          <small>Academic Project · 2026</small>
        </div>

      </aside>

      {/* MAIN CONTENT */}
      <main className="main-content">

        {/* TOPBAR */}
        <header className="topbar">

          <div>
            <span className="breadcrumb">WORKSPACE /</span>

            <span className="current-page">
              {selectedDetection ? " Detection Details" : ` ${page}`}
            </span>
          </div>

          <button
            className="refresh-button"
            onClick={loadHistory}
          >
            ↻ Refresh
          </button>

        </header>

        <section className="page-content">

          {/* NORMAL PAGE HEADING */}
          {!selectedDetection && (
            <div className="page-heading">

              <div>
                <div className="eyebrow">
                  SECURITY OPERATIONS CENTER
                </div>

                <h1>
                  {page === "Overview"
                    ? "Threat Overview"
                    : page === "History"
                    ? "Detection History"
                    : "Threat Detection"}
                </h1>

                <p>
                  Monitor network traffic and identify suspicious activities.
                </p>
              </div>

              <div className="live-label">
                <span className="status-dot"></span>
                API CONNECTION
              </div>

            </div>
          )}

          {/* SUCCESS AND ERROR MESSAGES */}
          {message && (
            <div className="message">
              {message}

              <button onClick={() => setMessage("")}>
                ×
              </button>
            </div>
          )}

          {/* ================================= */}
          {/* THREAT DETAILS PAGE */}
          {/* ================================= */}

          {selectedDetection ? (
            <ThreatDetails
              detection={selectedDetection}
              onBack={closeDetection}
            />
          ) : (

            <>

              {/* ================================= */}
              {/* OVERVIEW PAGE */}
              {/* ================================= */}

              {page === "Overview" && (
                <>

                  <div className="stats-grid">

                    <StatCard
                      label="TOTAL FLOWS"
                      value={total}
                      icon="▤"
                    />

                    <StatCard
                      label="DETECTED ATTACKS"
                      value={attacks.length}
                      icon="⚠"
                      color="red"
                    />

                    <StatCard
                      label="BENIGN TRAFFIC"
                      value={benign.length}
                      icon="✓"
                      color="green"
                    />

                    <StatCard
                      label="HIGH / CRITICAL RISK"
                      value={highRisk.length}
                      icon="◈"
                      color="orange"
                    />

                  </div>

                  <div className="content-grid">

                    {/* ATTACK DISTRIBUTION */}
                    <div className="panel">

                      <div className="panel-heading">
                        <div>
                          <h3>Attack Distribution</h3>
                          <p>Detected attack types in saved records</p>
                        </div>
                      </div>

                      {sortedAttacks.length === 0 ? (
                        <EmptyState text="No attacks recorded yet." />
                      ) : (

                        <div className="attack-list">

                          {sortedAttacks.map(([name, count]) => (
                            <div className="attack-row" key={name}>

                              <div className="attack-info">
                                <span>{name}</span>
                                <strong>{count}</strong>
                              </div>

                              <div className="progress-track">
                                <div
                                  className="progress-fill"
                                  style={{
                                    width: `${
                                      (count / attacks.length) * 100
                                    }%`,
                                  }}
                                ></div>
                              </div>

                            </div>
                          ))}

                        </div>
                      )}

                    </div>

                    {/* RECENT DETECTIONS */}
                    <div className="panel">

                      <div className="panel-heading">

                        <div>
                          <h3>Recent Detections</h3>
                          <p>Latest saved network flows</p>
                        </div>

                        <button
                          className="text-button"
                          onClick={() => navigateTo("History")}
                        >
                          View all →
                        </button>

                      </div>

                      <HistoryTable
                        records={history.slice(0, 5)}
                        onSelect={openDetection}
                      />

                    </div>

                  </div>

                </>
              )}

              {/* ================================= */}
              {/* THREAT DETECTION / UPLOAD PAGE */}
              {/* ================================= */}

              {page === "Threat Detection" && (

                <div className="panel upload-panel">

                  <div className="upload-icon">⇧</div>

                  <h2>Upload Network Traffic CSV</h2>

                  <p>
                    Upload a CICIDS2017-compatible CSV file to analyse
                    network traffic using your trained Random Forest model.
                  </p>

                  <label
                    className="file-picker"
                    htmlFor="csv-upload"
                  >
                    <span>Choose CSV file</span>

                    <small>
                      {selectedFile
                        ? selectedFile.name
                        : "No file selected"}
                    </small>
                  </label>

                  <input
                    id="csv-upload"
                    type="file"
                    accept=".csv"
                    onChange={(e) =>
                      setSelectedFile(e.target.files[0] || null)
                    }
                  />

                  <button
                    className="primary-button"
                    onClick={uploadCSV}
                    disabled={uploading}
                  >
                    {uploading
                      ? "Analysing traffic..."
                      : "Run Threat Detection"}
                  </button>

                  <div className="upload-note">
                    Results will be saved automatically in MongoDB.
                  </div>

                </div>

              )}

              {/* ================================= */}
              {/* HISTORY PAGE */}
              {/* ================================= */}

              {page === "History" && (

                <div className="panel">

                  <div className="panel-heading">

                    <div>
                      <h3>All Detection Records</h3>
                      <p>
                        Records retrieved from MongoDB through FastAPI
                      </p>
                    </div>

                    <span className="record-count">
                      {total} records
                    </span>

                  </div>

                  <HistoryTable
                    records={history}
                    onSelect={openDetection}
                  />

                  {loading && (
                    <p className="loading-text">
                      Loading records...
                    </p>
                  )}

                </div>

              )}

            </>
          )}

        </section>

      </main>

    </div>
  );
}


// =================================
// STATISTICS CARD
// =================================

function StatCard({
  label,
  value,
  icon,
  color = "blue",
}) {
  return (
    <div className="stat-card">

      <div className="stat-top">
        <span>{label}</span>

        <span className={`stat-icon ${color}`}>
          {icon}
        </span>
      </div>

      <strong>{value}</strong>

      <small>Based on saved detection history</small>

    </div>
  );
}


// =================================
// HISTORY TABLE
// =================================

function HistoryTable({ records, onSelect }) {

  if (!records.length) {
    return <EmptyState text="No detection records found." />;
  }

  return (

    <div className="table-wrapper">

      <table>

        <thead>
          <tr>
            <th>FLOW</th>
            <th>DETECTION</th>
            <th>CONFIDENCE</th>
            <th>RISK SCORE</th>
            <th>LEVEL</th>
            <th>DETAILS</th>
          </tr>
        </thead>

        <tbody>

          {records.map((item, index) => (

            <tr key={item._id || index}>

              <td>#{item.flow_id ?? index + 1}</td>

              <td className="attack-name">
                {item.prediction || "Unknown"}
              </td>

              <td>
                {item.confidence ?? "N/A"}%
              </td>

              <td>
                {item.risk_score ?? "N/A"}/100
              </td>

              <td>
                <span
                  className={`risk-badge ${
                    item.risk_level?.toLowerCase() || ""
                  }`}
                >
                  {item.risk_level || "Unknown"}
                </span>
              </td>

              <td>
                <button
                  className="text-button"
                  onClick={() => onSelect(item)}
                >
                  View Details →
                </button>
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}


// =================================
// THREAT DETAILS PAGE
// =================================

function ThreatDetails({ detection, onBack }) {

  const isAttack = detection.prediction !== "BENIGN";

  const riskLevel = detection.risk_level || "Unknown";

  const riskReason =
    detection.risk_reason ||
    detection.reason ||
    "No additional risk explanation was saved for this detection.";

  return (

    <div className="detail-page">

      {/* DETAILS HEADER */}
      <div className="detail-toolbar">

        <div>
          <h2>Threat Analysis Details</h2>

          <p>
            Individual network flow detection report
          </p>
        </div>

        <button
          className="refresh-button"
          onClick={onBack}
        >
          ← Back
        </button>

      </div>

      {/* DETECTION SUMMARY */}
      <div className="detail-summary">

        <div>

          <span className="detail-label">
            DETECTION RESULT
          </span>

          <h2 className={isAttack ? "threat-text" : "benign-text"}>
            {detection.prediction || "Unknown"}
          </h2>

          <p>
            Flow ID: #{detection.flow_id ?? "N/A"}
          </p>

        </div>

        <span
          className={`risk-badge large ${
            riskLevel.toLowerCase()
          }`}
        >
          {riskLevel} Risk
        </span>

      </div>

      {/* DETECTION METRICS */}
      <div className="detail-grid">

        <div className="detail-card">
          <span className="detail-label">
            CONFIDENCE
          </span>

          <strong>
            {detection.confidence ?? "N/A"}%
          </strong>
        </div>

        <div className="detail-card">
          <span className="detail-label">
            RISK SCORE
          </span>

          <strong>
            {detection.risk_score ?? "N/A"}/100
          </strong>
        </div>

        <div className="detail-card">
          <span className="detail-label">
            RISK LEVEL
          </span>

          <strong>
            {riskLevel}
          </strong>
        </div>

        <div className="detail-card">
          <span className="detail-label">
            FLOW ID
          </span>

          <strong>
            #{detection.flow_id ?? "N/A"}
          </strong>
        </div>

      </div>

      {/* RISK EXPLANATION */}
      <div className="panel detail-explanation">

        <div className="panel-heading">

          <div>
            <h3>
              <span className="explanation-icon">◈ </span>
              Risk Explanation
            </h3>

            <p>
              Explanation returned by the detection system
            </p>
          </div>

        </div>

        <p>
          {riskReason}
        </p>

      </div>

      {/* INTERPRETATION */}
      <div className="panel detail-explanation">

        <div className="panel-heading">

          <div>
            <h3>Detection Interpretation</h3>
            <p>Understanding this prediction</p>
          </div>

        </div>

        <ul className="interpretation-list">

          <li>
            <strong>Prediction:</strong>{" "}
            {isAttack
              ? "The model classified this flow as an attack."
              : "The model classified this flow as benign traffic."}
          </li>

          <li>
            <strong>Confidence:</strong>{" "}
            Indicates the model's confidence in its predicted class.
          </li>

          <li>
            <strong>Risk score:</strong>{" "}
            A score assigned by the project's preliminary risk rules.
          </li>

          <li>
            <strong>Risk level:</strong>{" "}
            {riskLevel} according to the project's risk assessment rules.
          </li>

        </ul>

      </div>

      {/* DISCLAIMER */}
      <div className="detail-disclaimer">

        <strong>Important note:</strong>{" "}
        This report displays the prediction and risk information
        stored for this flow. The original network feature values
        are not currently stored in the detection history.
        Model predictions should not be treated as guaranteed
        real-world threat confirmation.

      </div>

    </div>
  );
}


// =================================
// EMPTY STATE
// =================================

function EmptyState({ text }) {
  return (
    <div className="empty-state">
      {text}
    </div>
  );
}


export default App;
