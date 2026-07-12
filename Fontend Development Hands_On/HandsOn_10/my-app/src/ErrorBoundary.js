import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Global Error Caught:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '40px', backgroundColor: '#ffe6e6', color: '#cc0000', textAlign: 'center' }}>
          <h2>Oops! Something went wrong.</h2>
          <p>Please refresh the page to try again.</p>
        </div>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundary;