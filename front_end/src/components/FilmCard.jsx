import PropTypes from 'prop-types';
import Skeleton from 'react-loading-skeleton';
import './FilmCard.css'

/** Returns a film card, which is composed of a film's cover art, and film
 * title underneath that
 */
function FilmCard({ posterPath, title, isLoading}) {
	// base path for all film covers
	const baseCoverUrl= `https://image.tmdb.org/t/p/w600_and_h900_bestv2`

	return (
		<div className="film-card">
			{isLoading ? (
				<>
					{/* Skeleton for poster */}
					<Skeleton id='skeleton-poster' height={420} width={280} />
					{/* Skeleton for title */}
					<Skeleton id='skeleton-title' width={254} height={38} style={{ marginTop: '10px' }} />
				</>
			) : (
				<>
					{/* movie cover */}
					<img 
						src={`${baseCoverUrl}${posterPath}`}
						alt={`${title}-cover`} 
						className="film-poster"
					/>
					{/* movie title */}
					<h3 className="film-title">{title}</h3>
				</>
			)}
		</div>
	);
}

// prop types for the component
FilmCard.propTypes = {
	posterPath: PropTypes.string,
	title: PropTypes.string,
	isLoading: PropTypes.bool,
  };

export default FilmCard;
