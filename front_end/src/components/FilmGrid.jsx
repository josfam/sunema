import { useEffect, useState } from 'react';
import './FilmGrid.css'
import FilmCard from './FilmCard';

function FilmGrid () {
	const [films, setFilms] = useState([]);  // State to hold the list of films
    const [error, setError] = useState(null); // Error state

	useEffect(() =>{
		// fetch films from the backend
		const getFilmsByWeather = async () => {
			try{
				const response = await fetch('/api/v1/films/by-weather', {
					method: 'get',
					headers: {
						'Content-Type': 'application/json'
					}
				})
				const data = await response.json();

				if (response.ok) {
					console.log('The data is :===> ', data); // DEBUG
					setFilms(Object.values(data.data));
				} else {
					setError('Failed to load films');
				}
			} catch (err) {
				console.log('Error while fetching films', err);
				setError('An error occurred while fetching films');
			}
		};
		getFilmsByWeather();
	}, []);

	if (error) {
		return (
		<div>{error}</div>
	);
	}

	return (
		<section id="home-film-container">
			{/* Map over films and render a film card for each film found */}
			{films.map(film => (
				<FilmCard
					key={film.id}
					posterPath={film.poster_path}
					title={film.title}
				/>
			))}
		</section>
	)
}

export default FilmGrid;
