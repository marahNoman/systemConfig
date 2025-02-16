from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("CONFIGURE_PROXY")
    class ConfigureProxyOperation(GenericOperation):
        """
        This operation will look for the environment variable CONFIGURE_PROXY_CONFIG_YAML,
        then inside that YAML file, it will find the key 'configure_proxy' and read steps_order, steps, etc.

        For example, if CONFIGURE_PROXY_CONFIG_YAML=/path/to/configure_proxy.yaml,
        it will load that file and expect something like:

            configure_proxy:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["configure_proxy"] in your YAML
            return "configure_proxy"
    