import { useEffect, useState } from 'react';
import './FilmGrid.css'
import FilmCard from './FilmCard';
import propTypes from 'prop-types';

function FilmGrid ({ temperature, setBannerMessage }) {
	const [films, setFilms] = useState([]);  // State to hold the list of films
    const [isLoading, setIsLoading] = useState(true); // for skeleton loading
	const [error, setError] = useState(null); // Error state

	useEffect(() =>{
		// fetch films from the backend
		const getFilmsByWeather = async () => {
			console.log(`[FilmGrid]-out The temperature is now ${temperature}`) // DEBUG
			if (temperature !== null && temperature !== undefined) {
				console.log(`[FilmGrid]-in The temperature is now ${temperature}`) // DEBUG
				try{
					const api_url = `/api/v1/films/by-weather?temperature=${temperature}`
					console.log(`api url temperature ===> `, api_url) // DEBUG
					const response = await fetch(api_url, {
						method: 'get',
						headers: {
							'Content-Type': 'application/json'
						}
					})
					const data = await response.json();
					
					if (response.ok) {
						console.log('The data is :===> ', data); // DEBUG
						setFilms(Object.values(data.data));
						if (data.source === 'samples') {
							const message = `You are seeing pre-selected sample films, because no TMBD API key was found.`
							setBannerMessage(message)
						} else {
							setBannerMessage('')
						}
					} else {
						setError('Failed to load films');
					}
				} catch (err) {
					console.log('Error while fetching films', err);
					setError('An error occurred while fetching films');
				} finally {
					setIsLoading(false); // stop loading when the data is fetched
				}
			};
		}
		getFilmsByWeather();
	}, [temperature, setBannerMessage]);

	if (error) {
		return (
		<div>{error}</div>
	);
	}

	return (
		<section id="home-film-container">
			{isLoading ? (
				// Render 6 skeleton placeholders while loading
                Array.from({ length: 6 }).map((_, index) => (
                    <FilmCard key={index} isLoading={true} />
                ))
			) : (
				/* Map over films and render a film card for each film found */
				films.map(film => (
				<FilmCard
					key={film.id}
					posterPath={film.poster_path}
					title={film.title}
					isLoading={false}
				/>
				))
			)}
		</section>
	);
}

FilmGrid.propTypes = {
	temperature: propTypes.number,
	setBannerMessage: propTypes.func
}

export default FilmGrid;
