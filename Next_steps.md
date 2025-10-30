# Next steps during development

- [x] Clarify asset hosting strategies
    - During the hackathons, only _raw_ Github urls worked
    - Git lfs and Github releases won't work. They are ultimately redirects that don't work like the _raw_ endpoints that the EDC consumers need.
    - Apart from that, we could use cloud storage, like Amazon S3. However, on the long run, this would mean duplicating cloud storage from where the CAD data are hosted (e.g. Cadenas), and from where meta data are hosted because the EDC mechanism assumes that providers provide a single REST-like API endpoint.
    As long as we need to zip those files together, it's not an ideal solution
    - [ ] Send Lenny a sketch with this problem



- [ ] Fix `.sdf` with intrinsic frame
    - See Lukasz comment:

    ```xml
    Example of attachment frame
    <frame name="ft_mount"
           attached_to="robot_flange_adapter_link"
           intrinsic:create_attachment_entity="true">
        <pose>0.0 0.0 0.02 0 0 0</pose>
    </frame>
    ```





--------------------------------------------------------------------------------
## Done
- [x] Implement a `build_asset.py` script
    - This should zip the respective files and put it into `assets/`
- [x] Fix units in the `.obj` files (divide by 1000)
    - Re-adapt the `.sdf`
