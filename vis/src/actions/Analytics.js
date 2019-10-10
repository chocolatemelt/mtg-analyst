export const FETCHING_SAMPL_DATA = 'FETCHING_SAMPL_DATA';
export const RECV_SAMPL_DATA = 'RECV_SAMPL_DATA';
export const FETCH_ERROR = 'FETCH_ERROR';

export function fetchingSampleData(isFetching) {
  return {
    type: FETCHING_SAMPL_DATA,
    isFetching,
  };
}

export function recvSampleData(data) {
  return {
    type: RECV_SAMPL_DATA,
    data,
  };
}

export function fetchError(msg) {
  return {
    type: FETCH_ERROR,
    msg,
  };
}
