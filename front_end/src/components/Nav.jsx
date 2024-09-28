import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import '../styles/Nav.css'

function Nav() {
	return (
	  <div className="home__top">
		<div id="hamburger-container">
        	<FontAwesomeIcon icon={faBars} className="bars" aria-hidden="true" />
		</div>
      </div>
	);
}

export default Nav;
