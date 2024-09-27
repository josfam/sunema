import { useState, useEffect } from "react";
import UserWeatherSection from "../components/UserWeather";
import FilmGrid from "../components/FilmGrid";
import Footer from "../components/Footer";
import Nav from "../components/Nav";
import InfoBanner from "../components/InfoBanner";
import "../styles/Home.scss";


function Home() {
  const [location, setLocation] = useState({ latitude: null, longitude: null });
  const [error, setError] = useState(null);
  const [temperature, setTemperature] = useState(null); // handles temperature state
  const [bannerMessage, setBannerMessage] = useState('');
  const [messageType, setMessageType] = useState('note')

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
	  <Nav/>
      <UserWeatherSection
		latitude={location.latitude}
		longitude={location.longitude}
		temperature={temperature} // pass temperature
		setTemperature={setTemperature} // pass the temperature setter function
	  />
	  {/* Render the info banner, only if there is a message there */}
	  {bannerMessage && <InfoBanner message={bannerMessage} messageType={messageType}/>}
      <FilmGrid
	  	temperature={temperature}
		setBannerMessage={setBannerMessage}
		setMessageType={setMessageType}
	  />
      {error ? <p>Error: {error}</p> : console.log(`Latitude: ${location.latitude}, Longitude: ${location.longitude}`)}
      <Footer />
    </div>
  );
}

export default Home;
