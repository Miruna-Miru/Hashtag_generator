import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [hashtags, setHashtags] = useState([]);
  const [darkMode, setDarkMode] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    document.body.className = darkMode ? 'dark' : 'light';
  }, [darkMode]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/generate', {
        content: inputText,
      });
      setHashtags(response.data.hashtags);
    } catch (err) {
      console.error('Error:', err);
      alert('Something went wrong 😢');
    }
    setLoading(false);
  };

  const handleCopyAll = () => {
    const tagString = hashtags.join(' ');
    navigator.clipboard.writeText(tagString);
    alert('📋 Hashtags copied to clipboard!');
  };

  return (
    <div className="App">
      <div className="theme-toggle">
        <button onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? '☀️' : '🌙'}
        </button>
      </div>

      <h1>#️⃣ Hashtag Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="10"
          placeholder="Enter your blog or post content here..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        ></textarea>
        <button type="submit">Generate Hashtags</button>
      </form>

      <div className="results">
        {loading ? (
          <div className="spinner">⚙️ Generating hashtags...</div>
        ) : (
          <>
            {hashtags.length > 0 && (
              <>
                <ul>
                  {hashtags.map((tag, idx) => (
                    <li key={idx}>{tag}</li>
                  ))}
                </ul>
                <button className="copy-btn" onClick={handleCopyAll}>
                  📋 Copy All
                </button>
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
