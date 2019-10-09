import { FETCHING_SAMPL_DATA, FETCH_SAMPL_DATA, FETCH_ERROR } from '../actions/Analytics';

const AnalyticsReducer = (
  state = {
    data: {},
    isFetching: false,
    error: undefined,
  },
  action
) => {
  switch (action.type) {
    case FETCHING_SAMPL_DATA:
      return {
        ...state,
        data: action.data,
      };
    case FETCH_SAMPL_DATA:
      return {
        ...state,
        isFetching: action.isFetching,
      };
    case FETCH_ERROR:
      return {
        ...state,
        error: action.msg,
      };
    default:
      return state;
  }
};

export default AnalyticsReducer;
