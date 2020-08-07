import React from "react";
import "./App.css";
import { Link } from "react-router-dom";
import ReactPlayer from "react-player";

function Video() {
  return (
    <div>
      <div>
        <h2>Here is a video explaining the science of what is happening</h2>
      </div>
      <div className="vid">
        <ReactPlayer url="https://www.youtube.com/watch?v=kOyPsl0bI1g" />
      </div>
    </div>
  );
}

export default Video;
