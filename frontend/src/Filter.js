import React, { useState, useEffect } from "react";
import axios from "axios";

//MaterialUI
import {  Table, Container } from 'react-bootstrap'




export default function Filter() {
  const searchValue = React.useRef("");
  const [searchTerm, setSearchTerm] = React.useState("CA");



  function searchBusiness() {
    setSearchTerm(searchValue.current.value);
  }

  function handleSubmit(e) {
    e.preventDefault();
  }


  const [data, setData] = useState({
    posts: [],
  });

  useEffect(() => {
    axios.get(`http://localhost:8000/files/search/?search=${searchTerm}`).then((res) => {
      setData({
        posts: res.data,
      });
      console.log(res.data);
      searchValue.current.focus();
    });
  }, [setData, searchTerm]);

  return (
    <Container >
      <section className="section">
      <h2 className="section-title">Search Businesses</h2>
      <form className="form search-form" onSubmit={handleSubmit}>
        <div className="form-control">
          <label htmlFor="name">search</label>
          <input
            type="text"
            name="name"
            id="name"
            ref={searchValue}
            onChange={searchBusiness}
          />
        </div>
      </form>
      </section>
      <Table striped bordered hover responsive className='table-sm'>
        <thead>
            <tr>
                <th>NAME</th>
                <th>INDUSTRY</th>
                <th>ADDRESS</th>
                <th>CITY</th>
                <th>STATE</th>
                <th>ZIP</th>
                <th>COUNTY</th>
                <th>PHONE</th>
                <th>FAX</th>
                <th>WEBSITE</th>
                <th>TITLE</th>
                <th>CONTACT</th>
                <th>NUMBER</th>
                <th>EMPLOYEE</th>
                <th>SALES</th>
                <th>RANGE</th>
                <th>SIC CODE</th>
                <th>DESCRIPTION</th>
                <th>CODE</th>
                <th>LATITUDE</th>
                <th>LONGITUDE</th>
            </tr>
        </thead>

        <tbody>
            {data.posts.map(business => (
                <tr key={business.id}>
                    <td>{business.name}</td>
                    <td>{business.industry}</td>
                    <td>{business.address}</td>
                    <td>{business.city}</td>
                    <td>{business.state}</td>
                    <td>{business.zip}</td>
                    <td>{business.county}</td>
                    <td>{business.phone}</td>
                    <td>{business.fax}</td>
                    <td>{business.website}</td>    
                    <td>{business.title}</td>
                    <td>{business.contact}</td>
                    <td>{business.number}</td>
                    <td>{business.employee}</td>
                    <td>{business.sales}</td>
                    <td>{business.range}</td>
                    <td>{business.sic}</td>
                    <td>{business.description}</td>
                    <td>{business.code}</td>
                    <td>{business.latitude}</td>
                    <td>{business.longitude}</td>      
                </tr>
            ))}
        </tbody>
       </Table>
    </Container>
  );
}
