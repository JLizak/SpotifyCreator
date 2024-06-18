import React, { useState, useEffect } from 'react'
import axios from 'axios'

function Test(){

    const [playlists, setPlaylists] = useState([])

useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/playlists/')
    .then(response => {
        setPlaylists(response.data);
    })
    .catch(error => {
        console.error("Error while fetching playlsits");
    })
}, [])

    return(
       <div>
        <h1>Playlists</h1>
        {playlists.map(playlist => (
            <div key={playlist.id}>
            <h2>{playlist.name}</h2>
            <ul>
                {playlist.songs.map(song => (
                    <li key={song.id}>{song.name}</li>
                ))}
            </ul>
            </div>
        ))}
       </div>
    )
}

export default Test