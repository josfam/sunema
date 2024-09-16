import { useState, useEffect } from "react";
import UserWeatherSection from "../components/UserWeather";
import "../styles/Home.css"

function Home() {
	const [location, setLocation] = useState({ latitude: null, longitude: null });
	const [error, setError] = useState(null);

	useEffect(() => {
	  // Check if browser supports Geolocation API
	  if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(
		  (position) => {
			// Success: set the user's location in state
			setLocation({
			  latitude: position.coords.latitude,
			  longitude: position.coords.longitude,
			});
		  },
		  (err) => {
			// Handle error
			console.log(err.message);
			// default location of Griffith Park, Mt. Hollywood, Los Angeles
			setLocation({
				latitude: 34.125330,
				longitude: -118.313030,
			});
			setError(null);
		  }
		);
	  } else {
		// Geolocation API not supported
		console.log('Geolocation is not supported by this browser.');
		// default location of Griffith Park, Mt. Hollywood, Los Angeles
		setLocation({
			latitude: 34.125330,
			longitude: -118.313030,
		});
		setError(null);
	  }
	}, []); // Empty dependency array ensures this runs once when the component mounts
  
	return (
	  <div className="home">
		<UserWeatherSection latitude={location.latitude} longitude={location.longitude}/>
		{error ? (
		  <p>Error: {error}</p>
		) : (
			// DEBUG log the longitude and latitude from the browser
			console.log(
				`Latitude(browser): ${location.latitude}\nLongitude(browser): ${location.longitude}`
			)
		)}
	  </div>
	);
}

export default Home;
