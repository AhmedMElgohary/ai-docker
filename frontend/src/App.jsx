// frontend/src/App.jsx
import { useState } from 'react'
import './App.css'

function App() {
  // 1. STATE VARIABLES (The memory of the app)
  const [inputText, setInputText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false); // To show "Thinking..."
  const [temperature, setTemperature] = useState(0.5); // Creativity slider

  // 2. THE FUNCTION THAT CALLS PYTHON
  const handleSummarize = async () => {
    setLoading(true); // Turn on loading spinner
    setSummary("");   // Clear old summary

    try {
      // The Fetch API: This is the phone call to Port 8000
      const response = await fetch("http://127.0.0.1:8000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          text: inputText, 
          temperature: parseFloat(temperature) 
        }),
      });

      const data = await response.json(); // Read the JSON response
      setSummary(data.summary); // Update the screen with the result

    } catch (error) {
      console.error("Error connecting to server:", error);
      setSummary("Error: Could not connect to the AI server.");
    }
    
    setLoading(false); // Turn off loading spinner
  };

  // 3. THE UI (What the user sees)
  return (
    <div className="app-container">
      <h1>AI Summarizer 🤖</h1>
      
      {/* Input Area */}
      <textarea 
        placeholder="Paste your long article here..." 
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        rows={10}
        cols={50}
      />

      {/* Controls */}
      <div className="controls">
        <label>Creativity: {temperature}</label>
        <input 
          type="range" 
          min="0.1" 
          max="1.0" 
          step="0.1" 
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
        />
        
        <button onClick={handleSummarize} disabled={loading}>
          {loading ? "Thinking..." : "Summarize"}
        </button>
      </div>

      {/* Result Area */}
      {summary && (
        <div className="result-box">
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  )
}

export default App