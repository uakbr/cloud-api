import React from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ScanPage from './pages/ScanPage';
import ResultsPage from './pages/ResultsPage';
import NotFoundPage from './pages/NotFoundPage';
import { useAuth } from './context/auth';

const PrivateRoute = ({ component: Component, ...rest }) => {
  const { authTokens } = useAuth();

  return (
    <Route
      {...rest}
      render={props =>
        authTokens ? (
          <Component {...props} />
        ) : (
          <Redirect to="/login" />
        )
      }
    />
  );
};

const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={HomePage} />
      <PrivateRoute path="/scan" component={ScanPage} />
      <PrivateRoute path="/results" component={ResultsPage} />
      <Route component={NotFoundPage} />
    </Switch>
  );
};

export default Routes;