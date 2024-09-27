import PropTypes from 'prop-types';
import './infoBanner.scss'

/** A general-purpose banner for showing informational messages
 * message types can be: note, warning, error
*/
const InfoBanner = function ( { message, messageType } ) {
	return (
		<section className={`info-banner info-${messageType}`}>
			<p>{message}</p>
		</section>
	);
}

InfoBanner.propTypes = {
	message: PropTypes.string,
	messageType: PropTypes.string.isRequired
}

export default InfoBanner;
