# CMS Progress


## 2022-09-22 
- I outlined a how the publishing workflow will work today and started experimenting with Colllection structures.
- Currently not working, I'll push code when it makes sense
- Current Focus:
  - Make sure that collection structure makes sense and is maintainable
    - A problem I identified during the first iteration was that we would either have a rediculouslyl long and repetitive config file, or a very complex page configuration. At that time I went the route of complex page configuration
  - Another major issue, is in our current setup, we haven't been able to access data without using things like `data[0].section.title etc. which is not maintainable.
    - This relates to nuxt content and how info is queried. At the time of setting up the original one, I identified that this could be an issue, it needs to be solved now as this will be a huge maintainability problem down the road
    - Key consideration:
      - What would this look like after 4 years of page creation and editing?
        - It could easily end up with way to many disorganized file
- Tomorrow Plan:
  - Create a config that groups pages by edition
  - Allow the creation of page content within each page
  - Try making two collections based on page type to account for major differences in page structures and info (landing pages and supporting pages are very different
    - use a slug focused system for organizing pages
- Next Steps:
  - After the collection issue is fixed and querying works properly, then move onto the live preview and publishing workflow.
  - Set up keywords in pushes etc to satisfy early identified issues with a git commit and push nightmare. Branching system needs to also be properly setup
  - Test editorial workflow by myself
  - Test it with someone else with admin and someone with editor access
    - Get developer feedback and feedback from previous user tester (not in the core team) on new schema
  - Merge Down
  - Follow up and Documentation
