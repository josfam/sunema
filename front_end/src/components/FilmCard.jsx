import PropTypes from 'prop-types';
import './FilmCard.css'

/** Returns a film card, which is composed of a film's cover art, and film
 * title underneath that
 */
function FilmCard({ posterPath, title }) {
	// base path for all film covers
	const baseCoverUrl= `https://image.tmdb.org/t/p/w600_and_h900_bestv2`

	return (
		<div className="film-card">
			{/* movie cover */}
			<img 
				src={`${baseCoverUrl}${posterPath}`}
				alt={`${title}-cover`} 
				className="film-poster"
			/>
			{/* movie title */}
			<h3 className="film-title">{title}</h3>
		</div>
	)
}

// prop types for the component
FilmCard.propTypes = {
	posterPath: PropTypes.string,
	title: PropTypes.string
  };

export default FilmCard;
