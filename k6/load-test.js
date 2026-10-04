import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 10,
};

export default function () {
    http.get('http://core-backend:8888/health');
    sleep(1);
}
