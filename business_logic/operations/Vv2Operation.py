from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("VV2")
    class Vv2Operation(GenericOperation):
        """
        This operation will look for the environment variable VV2_CONFIG_YAML,
        then inside that YAML file, it will find the key 'vv2' and read steps_order, steps, etc.

        For example, if VV2_CONFIG_YAML=/path/to/vv2.yaml,
        it will load that file and expect something like:

            vv2:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["vv2"] in your YAML
            return "vv2"
    