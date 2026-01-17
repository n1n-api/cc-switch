import { ProviderAPIConfig } from '../types';

const N1NAPIConfig: ProviderAPIConfig = {
    getBaseURL: () => 'https://api.n1n.ai/v1',
    headers: ({ providerOptions }) => {
        return { Authorization: `Bearer ${providerOptions.apiKey}` };
    },
    getEndpoint: ({ fn }) => {
        switch (fn) {
            case 'chatComplete':
                return '/chat/completions';
            default:
                return '';
        }
    },
};

export default N1NAPIConfig;
