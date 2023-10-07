import React, { useReducer } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import ScanPage from './pages/ScanPage';
import ResultsPage from './pages/ResultsPage';
import NotFoundPage from './pages/NotFoundPage';
import { initialState, reducer } from './store/reducer';
import { StateContext } from './store/StateContext';

const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <StateContext.Provider value={{ state, dispatch }}>
      <Router>
        <Header />
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/scan" component={ScanPage} />
          <Route path="/results" component={ResultsPage} />
          <Route component={NotFoundPage} />
        </Switch>
        <Footer />
      </Router>
    </StateContext.Provider>
  );
};

export default App;