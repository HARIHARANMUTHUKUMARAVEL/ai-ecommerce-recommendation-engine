import { useState } from "react";
import { getRecommendations } from "./api";

function App() {
  const [productId, setProductId] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    try {
      const data = await getRecommendations(productId);
      setRecommendations(data);
      setError("");
    } catch (err) {
      setError("Invalid Product ID or backend error");
      setRecommendations([]);
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>AI Enabled Recommendation Engine</h2>

      <input
        type="number"
        placeholder="Enter Product ID"
        value={productId}
        onChange={(e) => setProductId(e.target.value)}
      />

      <button onClick={handleSubmit}>Get Recommendations</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {recommendations.length > 0 && (
        <ul>
          {recommendations.map((item, index) => (
            <li key={index}>Recommended Product ID: {item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
