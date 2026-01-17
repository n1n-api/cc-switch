from datetime import datetime
from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.model_entities import ModelType
from core.model_runtime.entities.provider_entities import (
    ConfigurateMethod,
    CredentialFormSchema,
    FormType,
    ProviderEntity,
    ProviderCredentialSchema,
)
from core.plugin.entities.plugin_daemon import PluginModelProviderEntity

N1N_PROVIDER_DECLARATION = ProviderEntity(
    provider="n1n",
    label=I18nObject(en_US="n1n.ai", zh_Hans="n1n.ai"),
    description=I18nObject(
        en_US="n1n.ai is a powerful AI model provider compatible with OpenAI API.",
        zh_Hans="n1n.ai 是一个强大的 AI 模型提供商，兼容 OpenAI API。"
    ),
    icon_small=I18nObject(en_US="https://n1n.ai/favicon.ico"),
    supported_model_types=[ModelType.LLM],
    configurate_methods=[ConfigurateMethod.CUSTOMIZABLE_MODEL],
    provider_credential_schema=ProviderCredentialSchema(
        credential_form_schemas=[
            CredentialFormSchema(
                variable="openai_api_key",
                label=I18nObject(en_US="API Key", zh_Hans="API Key"),
                type=FormType.SECRET_INPUT,
                required=True,
                placeholder=I18nObject(en_US="Enter your n1n.ai API Key", zh_Hans="请输入您的 n1n.ai API Key"),
            )
        ]
    )
)

def get_n1_provider_entity(tenant_id: str) -> PluginModelProviderEntity:
    return PluginModelProviderEntity(
        id="n1n",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        provider="n1n",
        tenant_id=tenant_id,
        plugin_unique_identifier="langgenius/n1n/n1n",
        plugin_id="langgenius",
        declaration=N1N_PROVIDER_DECLARATION
    )
