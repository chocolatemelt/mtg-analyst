export const FETCH_SAMPL_DATA = 'FETCH_SAMPL_DATA';
export const FETCHING_SAMPL_DATA = 'FETCHING_SAMPL_DATA';
export const FETCH_ERROR = 'FETCH_ERROR';

export function fetchSampleData(data) {
  return {
    type: FETCH_SAMPL_DATA,
    data,
  };
}

export function fetchingSampleData(isFetching) {
  return {
    type: FETCHING_SAMPL_DATA,
    isFetching,
  };
}

export function fetchError(msg) {
  return {
    type: FETCH_ERROR,
    msg,
  };
}
