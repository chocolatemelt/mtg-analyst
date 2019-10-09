import React from 'react';
import ReactDOM from 'react-dom';

import Root from './containers/Root';
import store from './configureStore';
import * as serviceWorker from './serviceWorker';
import 'normalize.css';
import 'bootstrap-css-only/css/bootstrap.css';
import './css/index.css';

ReactDOM.render(<Root store={store} />, document.getElementById('root'));

serviceWorker.register();
