import { useState, useEffect } from "react";
import PropTypes from 'prop-types';
import "./UserWeather.css"

/** For the section of the home page that has the user greeting, and the weather
 * details
*/
function UserWeatherSection ( { latitude, longitude, temperature, setTemperature } ) {
	// state to store weather data
	const [ icon, setIcon ] = useState(null);
	const [ error, setError ] = useState(null);

	useEffect(() => {
		if (latitude && longitude) {
			const getWeather = async function(){
			try {
				const response = await fetch(
				`/api/v1/weather/current?lat=${latitude}&lon=${longitude}`, {
					method: 'get',
					headers: {
						'Content-Type': 'application/JSON'
					}
				});
				console.log('Response status:', response.status); // DEBUG
				const info = await response.json();
				console.log(info);
				// only set temperature and icon if the data actually exists
				if (response.ok && info.data && info.data.main) {	
					setTemperature(info.data.main.temp);
					setIcon(info.data.weather[0].icon)
				} else {
					setError(info.message);
				}
			} catch (error) {
				console.log(`error`, error);
			}};
			getWeather();
		}
	}, [latitude, longitude, setTemperature]);


	return (
		<section className="userWeather">
		<h2 id="user-greeting">Hello!</h2>
		{/* Conditional rendering of temperature or error message */}
		{error ? (
			<div className="error-message">
				<p>Error: {error}</p>
			</div>
		) : (
		<div className="weather-icon-container">
			{/* load placeholder image as temperature is being fetched */}
			<div id="temperature-number">{ temperature ? `${temperature.toFixed(1)} °C` : `⏳`}</div>
			<img
				id="weather-icon"
				src={`http://openweathermap.org/img/wn/${icon}.png`}
				alt="Weather icon"
			/>
		</div>
		)}
		</section>
	);
};

// prop types for the component
UserWeatherSection.propTypes = {
	latitude: PropTypes.number,
	longitude: PropTypes.number,
	setTemperature: PropTypes.func.isRequired,
	temperature: PropTypes.number
  };

export default UserWeatherSection;
