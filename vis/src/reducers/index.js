import { combineReducers } from 'redux';
import AnalyticsReducer from './Analytics';

const rootReducer = combineReducers({
  analytics: AnalyticsReducer,
});

export default rootReducer;
