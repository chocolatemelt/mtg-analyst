export const FETCHING_SAMPL_DATA = 'FETCHING_SAMPL_DATA';
export const RECV_SAMPL_DATA = 'RECV_SAMPL_DATA';
export const FETCH_ERROR = 'FETCH_ERROR';

export const fetchingSampleData = isFetching => ({
  type: FETCHING_SAMPL_DATA,
  isFetching,
});

export const recvSampleData = data => ({
  type: RECV_SAMPL_DATA,
  data,
});

export const fetchError = msg => ({
  type: FETCH_ERROR,
  msg,
});
