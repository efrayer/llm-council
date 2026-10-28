import './Header.css'

function Header() {
  return (
    <header className="site-header">
      <div>
        <h1 className="site-title">LLM Council</h1>
        <p className="site-subtitle">GPT 6.1 Terra - Gemini 4 Argon - Claude Sonnet 5.5</p>
      </div>
      <a className="site-link" href="https://thinkdataanalysis.com" target="_blank" rel="noreferrer">
        ThinkDataAnalysis.com
      </a>
    </header>
  )
}

export default Header
