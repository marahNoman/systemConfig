from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("P")
    class POperation(GenericOperation):
        """
        This operation will look for the environment variable P_CONFIG_YAML,
        then inside that YAML file, it will find the key 'p' and read steps_order, steps, etc.

        For example, if P_CONFIG_YAML=/path/to/p.yaml,
        it will load that file and expect something like:

            p:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["p"] in your YAML
            return "p"
    