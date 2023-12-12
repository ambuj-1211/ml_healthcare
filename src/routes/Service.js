import React from 'react';
import Footer from '../components/Footer';
import Navbar from "../components/Navbar";
import ServicePage from '../components/ServicePage';
import styles from '../constants/style';


const API_KEY ="YOUR_API_KEY_HERE"


const Service = () => {
  return (
    <div>
      <Navbar />
      <div className={`bg-white ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <ServicePage />
          </div>
      </div>
      <Footer />
    </div>
  )
}

export default Service