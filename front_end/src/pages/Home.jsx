import { useState, useEffect } from "react";
import UserWeatherSection from "../components/UserWeather";
import FilmGrid from "../components/FilmGrid";
import "../styles/Home.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";

function Home() {
  const [location, setLocation] = useState({ latitude: null, longitude: null });
  const [error, setError] = useState(null);

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
          });
        },
        (err) => {
          console.log(err.message);
          setLocation({
            latitude: 34.125330,
            longitude: -118.313030,
          });
          setError(null);
        }
      );
    } else {
      console.log('Geolocation is not supported by this browser.');
      setLocation({
        latitude: 34.125330,
        longitude: -118.313030,
      });
      setError(null);
    }
  }, []);

  return (
    <div className="home">
      <div className="home__top">
        <FontAwesomeIcon icon={faBars} className="bars" aria-hidden="true" />
      </div>
      <UserWeatherSection latitude={location.latitude} longitude={location.longitude} />
      <FilmGrid />
      {error ? <p>Error: {error}</p> : console.log(`Latitude: ${location.latitude}, Longitude: ${location.longitude}`)}
      <div className="bottom">
        <FontAwesomeIcon icon={faGithub} className="git" aria-hidden="true" />
      </div>
    </div>
  );
}

export default Home;
