import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import './Footer.scss';

function Footer() {
	return (
		<div className="bottom">
        <FontAwesomeIcon icon={faGithub} className="git" aria-hidden="true" />
      </div>
	);
}

export default Footer;
