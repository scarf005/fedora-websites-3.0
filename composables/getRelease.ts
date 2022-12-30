
export const getRelease = async () => {
  let { data } = await useAsyncData("release-data", () => {
    return queryContent()
      .where({ _file: "release.yml" })
      .findOne();
  });
  return data;
}
