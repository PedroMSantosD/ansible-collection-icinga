from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
    name: icinga2_timeperiod
'''

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(required=True, type='str'),
            display_name=dict(type='str'),
            ranges=dict(type='dict'),
            prefer_includes=dict(type='bool'),
            excludes=dict(type='list', elements='str'),
            includes=dict(type='list', elements='str')
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')

    module.exit_json(
        changed=False,
        args=args,
        name=name,
        order=str(order),
        state=state,
        file=file
    )


if __name__ == '__main__':
    main()
