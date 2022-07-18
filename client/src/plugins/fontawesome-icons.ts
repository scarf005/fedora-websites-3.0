import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// TODO: Fix this ASAP [Vue plugin docs](https://vuejs.org/guide/reusability/plugins.html)

// import solid icons
import { faBars } from "@fortawesome/free-solid-svg-icons";

// import brand icons
import { faFedora } from "@fortawesome/free-brands-svg-icons";

// add icons to the library here
library.add(faFedora, faBars);

export default { FontAwesomeIcon, library };
