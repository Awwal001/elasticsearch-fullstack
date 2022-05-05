import React, { useState } from 'react';
import './App.css';
import Filter from './Filter';

function App() {

  const [ file, setFile ] = useState(null);
  const [ title, setTitle ] = useState("");

  const fileUpload = () => {
    let uploadData = new FormData();
    uploadData.append('files', file, file.name);
    uploadData.append('title', title);

    fetch('http://localhost:8000/files/upload/', {
      method: 'POST',
      body: uploadData,
    })
    .then( res => console.log(res))
    .catch(error => console.log(error))
  }

  return (
    <React.Fragment>
      <div className="App">
        <h3>Upload Files</h3>
        <label>
          Title
          <input type="text" value={title} onChange={(evt) => setTitle(evt.target.value)}/>
        </label>
        <br/>
        <label>
          File
          <input type="file" onChange={(evt) => setFile(evt.target.files[0])}/>
        </label>
        <br/>
        <button onClick={() => fileUpload()}>Upload</button>
      </div>
      <Filter/>
    </React.Fragment>
  );
}

export default App;
