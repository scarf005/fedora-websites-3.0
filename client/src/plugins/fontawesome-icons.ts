import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// import solid icons
import { faBars } from "@fortawesome/free-solid-svg-icons";

// import brand icons
import { faFedora } from "@fortawesome/free-brands-svg-icons";

// add icons to the library here
library.add(faFedora, faBars);

/*export default function (app: any) {
  app.component("font-awesome-icon", FontAwesomeIcon)
  return app;
}

*/
export default FontAwesomeIcon