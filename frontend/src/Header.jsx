import './Header.css'
import headerImage from './assets/header-banner.png'

function Header() {
  return (
    <header className="site-header">
      <img 
        src={headerImage} 
        alt="LLM Council - Compare AI Model Responses" 
        className="header-image"
      />
    </header>
  )
}

export default Header
