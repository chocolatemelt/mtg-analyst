import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { createLogger } from 'redux-logger';
import rootReducer from './reducers';

export function configureStore(preloadedState) {
  let middleware = [thunkMiddleware];

  if (process.env.NODE_ENV !== 'production') {
    const loggerMiddleware = createLogger();
    middleware = [...middleware, loggerMiddleware];
  }

  const store = applyMiddleware(...middleware)(createStore)(
    rootReducer,
    preloadedState,
    /* eslint-disable no-underscore-dangle */
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    /* eslint-enable */
  );

  return store;
}

const store = configureStore();

export default store;
