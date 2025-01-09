from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("VV")
    class VvOperation(GenericOperation):
        """
        This operation will look for the environment variable VV_CONFIG_YAML,
        then inside that YAML file, it will find the key 'vv' and read steps_order, steps, etc.

        For example, if VV_CONFIG_YAML=/path/to/vv.yaml,
        it will load that file and expect something like:

            vv:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["vv"] in your YAML
            return "vv"
    