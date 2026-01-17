import { ProviderConfigs } from '../types';
import N1NAPIConfig from './api';
import {
    N1NChatCompleteConfig,
    N1NChatCompleteResponseTransform,
    N1NChatCompleteStreamChunkTransform,
} from './chatComplete';

const N1NConfig: ProviderConfigs = {
    chatComplete: N1NChatCompleteConfig,
    api: N1NAPIConfig,
    responseTransforms: {
        chatComplete: N1NChatCompleteResponseTransform,
        'stream-chatComplete': N1NChatCompleteStreamChunkTransform,
    },
};

export default N1NConfig;
