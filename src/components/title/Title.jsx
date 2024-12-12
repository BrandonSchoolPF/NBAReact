import React from 'react';

// A functional component that displays a title
const Title = ({ text, style }) => {
  return (
    <h1 style={style}>
      {text}
    </h1>
  );
};

// Default export for reuse
export default Title;