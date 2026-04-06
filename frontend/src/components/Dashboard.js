import React, { useState } from "react";
import axios from "axios";
import { Bar, Doughnut } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
);

function Dashboard() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const res = await axios.post("http://127.0.0.1:5000/analyze", {
      text: text,
    });
    setResult(res.data);
  };

  const sentimentColor = () => {
    if (!result) return "#999";
    if (result.sentiment === "positive") return "#22c55e";
    if (result.sentiment === "negative") return "#ef4444";
    return "#f59e0b";
  };

  // 📊 REAL DATA FROM HISTORY
  const counts = {
    positive: 0,
    negative: 0,
    neutral: 0,
  };

  if (result) {
    result.history.forEach((s) => counts[s]++);
  }

  const pieData = {
    labels: ["Positive", "Negative", "Neutral"],
    datasets: [
      {
        data: [counts.positive, counts.negative, counts.neutral],
        backgroundColor: ["#22c55e", "#ef4444", "#f59e0b"],
      },
    ],
  };

  const barData = {
    labels: ["Confidence"],
    datasets: [
      {
        label: "Confidence %",
        data: [result ? result.confidence * 100 : 0],
        backgroundColor: "#6366f1",
      },
    ],
  };

  return (
    <div style={mainContainer}>
      <div style={content}>
        <h1 style={title}>Customer Feedback Analyzer</h1>

        <div style={card}>
          <textarea
            style={textarea}
            placeholder="Enter feedback..."
            onChange={(e) => setText(e.target.value)}
          />
          <button style={button} onClick={analyze}>
            Analyze
          </button>
        </div>

        {result && (
          <>
            <div style={grid}>
              <div style={card}>
                <h3>Sentiment</h3>
                <h1 style={{ color: sentimentColor() }}>
                  {result.sentiment.toUpperCase()}
                </h1>
                <p>{(result.confidence * 100).toFixed(2)}%</p>
              </div>

              <div style={card}>
                <h3>Keywords</h3>
                {result.keywords.map((k, i) => (
                  <span key={i} style={tag}>{k}</span>
                ))}
              </div>

              <div style={card}>
                <h3>Insights</h3>
                <ul>
                  {result.insights.map((i, idx) => (
                    <li key={idx}>{i}</li>
                  ))}
                </ul>
              </div>
            </div>

            <div style={grid}>
              <div style={card}>
                <h3>Confidence</h3>
                <Bar data={barData} />
              </div>

              <div style={card}>
                <h3>Sentiment Distribution</h3>
                <Doughnut data={pieData} />
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

// 🎨 Styles
const mainContainer = {
  background: "#0f172a",
  minHeight: "100vh",
  color: "white",
};

const content = {
  padding: "30px",
};

const title = {
  marginBottom: "20px",
};

const grid = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
  gap: "20px",
};

const card = {
  background: "#1e293b",
  padding: "20px",
  borderRadius: "10px",
};

const textarea = {
  width: "100%",
  padding: "10px",
  borderRadius: "5px",
};

const button = {
  marginTop: "10px",
  padding: "10px",
  width: "100%",
  background: "#6366f1",
  color: "white",
  border: "none",
};

const tag = {
  background: "#334155",
  padding: "5px 10px",
  margin: "5px",
  borderRadius: "5px",
  display: "inline-block",
};

export default Dashboard;