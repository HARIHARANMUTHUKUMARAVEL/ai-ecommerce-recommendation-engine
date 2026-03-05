import { useState } from "react";
import { getRecommendations } from "./api";
import "./App.css";

function Dashboard() {

  const [productId, setProductId] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSubmit = async () => {

    setLoading(true);
    setError("");
    setHasSearched(true);

    try {

      const data = await getRecommendations(productId);
      setRecommendations(data);

    } catch (err) {

      setError("Invalid Product ID or backend error.");
      setRecommendations([]);

    }

    setLoading(false);

  };

  const icons = ["📱","💻","🎧","⌚","🎮","📷"];

  return (

    <div className="app-container">

      <h1>AI Recommendation Engine</h1>

      <input
        type="number"
        placeholder="Enter Product ID"
        value={productId}
        onChange={(e)=>setProductId(e.target.value)}
      />

      <button onClick={handleSubmit}>Get Recommendations</button>

      {error && <p className="error">{error}</p>}

      {hasSearched && recommendations.length > 0 && (

        <div className="recommendations-grid">

          {recommendations.map((item,index)=>(
            <div className="recommendation-card" key={index}>

              <div className="product-icon">
                {icons[index % icons.length]}
              </div>

              <div className="product-id">{item}</div>
              <div className="product-label">Product ID</div>

            </div>
          ))}

        </div>

      )}

    </div>

  );

}

export default Dashboard;