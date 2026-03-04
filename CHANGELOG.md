# Changelog

## [0.3.0](https://github.com/crackedngineer/codeurcv/compare/codeurcv-v0.2.0...codeurcv-v0.3.0) (2026-03-04)


### Features

* enhance PDF generation by using temporary directory and add filename validation ([a8d5331](https://github.com/crackedngineer/codeurcv/commit/a8d533154c9c99061733136238d3d9ef845eefa5))

## [0.2.0](https://github.com/crackedngineer/codeurcv/compare/codeurcv-v0.1.1...codeurcv-v0.2.0) (2026-03-04)


### Features

* implement dependency checker and update version to 0.1.1 ([2c83dc2](https://github.com/crackedngineer/codeurcv/commit/2c83dc2f28879e9b8feb0a27f93b79d44cca7356))

## [0.1.1](https://github.com/crackedngineer/codeurcv/compare/codeurcv-v0.1.0...codeurcv-v0.1.1) (2026-03-04)


### Bug Fixes

* update codeurcv version to 0.1.0 and adjust package configuration ([877cd54](https://github.com/crackedngineer/codeurcv/commit/877cd54c3ebf3d3a92c01b53c7b624c9b79497bc))

## [0.1.0](https://github.com/crackedngineer/codeurcv/compare/codeurcv-v0.0.1...codeurcv-v0.1.0) (2026-03-04)


### Features

* add GitHub Actions workflow for CV building ([9b4f983](https://github.com/crackedngineer/codeurcv/commit/9b4f9838d313c0d35563afd07874e56cce2c3f36))
* add release automation with Release Please configuration and manifest ([85a03f5](https://github.com/crackedngineer/codeurcv/commit/85a03f5f9291628b69b8baaf78926d454865950d))
* add release-please workflow configuration ([14cf9ed](https://github.com/crackedngineer/codeurcv/commit/14cf9ed03d59bdfacca9156170b3b232867c0eea))
* enable manual triggering of PDF build workflow ([5f616eb](https://github.com/crackedngineer/codeurcv/commit/5f616eb5156202c9be1b54b075319bd16ad6f7a8))
* enhance project descriptions and links in resume template for improved clarity and detail ([fd022b1](https://github.com/crackedngineer/codeurcv/commit/fd022b1ba995be381001f978ce3633c2ab42c3f0))
* enhance resume structure by adding summary and technical skills sections, update config and rendering logic ([0bf6eec](https://github.com/crackedngineer/codeurcv/commit/0bf6eec8c72e7f7204afae13196724946997397a))
* enhance resume template and rendering with regex support and additional links ([7f8d4eb](https://github.com/crackedngineer/codeurcv/commit/7f8d4ebde3321dabdddf5c54326eb40ce713b165))
* initialize project with Docker setup, LaTeX template, and resume generation scripts ([69e141f](https://github.com/crackedngineer/codeurcv/commit/69e141f9a8a49b9816150507d7d01c224e898c7a))
* update configuration file name from resume.yml to config.yml and add .vscode to .gitignore ([f5215c9](https://github.com/crackedngineer/codeurcv/commit/f5215c9ba0692aa39240ae1eff709c98794afd8c))
* update resume structure and enhance project details with links and technologies ([5ffd984](https://github.com/crackedngineer/codeurcv/commit/5ffd984a2c4dae21a3c98ce6e1a19b20d5256d23))


### Bug Fixes

* add git installation to Dockerfile for improved build environment ([11b587b](https://github.com/crackedngineer/codeurcv/commit/11b587b6ec3af5b97988343fe0c2ed07bae2b928))
* add links to project items in resume ([1c1dafa](https://github.com/crackedngineer/codeurcv/commit/1c1dafa04687d331aca1d05231b26cfab7449661))
* add Makefile to .dockerignore and update docker-build.yml paths ([134099b](https://github.com/crackedngineer/codeurcv/commit/134099b5a4dfb1c24a2c806862cd01dce6cb2f2e))
* add missing LaTeX packages to installation step in GitHub Action ([1eff6c3](https://github.com/crackedngineer/codeurcv/commit/1eff6c35a2b1233e490b167fc3029bbae5935623))
* add Pandoc feature to devcontainer configuration ([3345f56](https://github.com/crackedngineer/codeurcv/commit/3345f566ac718807405059ff2ff4eed4da3084cc))
* add pandoc to Dockerfile for enhanced document processing capabilities ([0fe0f97](https://github.com/crackedngineer/codeurcv/commit/0fe0f979dabfc48f40bb34260fbee67126e06499))
* add step to mark workspace as safe in build workflow ([dcda2dc](https://github.com/crackedngineer/codeurcv/commit/dcda2dc17c576c40233319e50c0f37ee5a8bd47d))
* adjust working directory for LaTeX compilation step in GitHub Actions ([588529e](https://github.com/crackedngineer/codeurcv/commit/588529e8a55b19dfd3df34a7ebf1cb12fa26e2f0))
* allow PDF compilation to continue on error in Makefile ([4c1c549](https://github.com/crackedngineer/codeurcv/commit/4c1c5491381b9a51fa1e5938f16d7eb3a68f256f))
* correct hyperlink syntax in resume heading for improved functionality ([e4ebbf5](https://github.com/crackedngineer/codeurcv/commit/e4ebbf56093c30c8f2bcd981ea9dfd48898a97e6))
* enhance achievements formatting in resume and improve API emphasis ([2b03abe](https://github.com/crackedngineer/codeurcv/commit/2b03abe2b06605ad68a1b07ac818e59e47366924))
* enhance project item command to include hyperlinks for better navigation ([7a909fa](https://github.com/crackedngineer/codeurcv/commit/7a909fa0f76346edbe295e6f8f5e9afff56652e5))
* ensure cleanup of auxiliary files in clean target of Makefile ([58574f6](https://github.com/crackedngineer/codeurcv/commit/58574f60e5e6a52d949e0200dcce8f9a23249ecd))
* ensure pdflatex runs on first compile in Makefile ([a80d536](https://github.com/crackedngineer/codeurcv/commit/a80d536121473b8069f1f000d61aacfe9d78c8ce))
* improve formatting in header section of LaTeX resume template ([1972330](https://github.com/crackedngineer/codeurcv/commit/19723305a1f07874b57082d0885e5ee835b6b29d))
* remove auxiliary and log files from output directory ([6c1833c](https://github.com/crackedngineer/codeurcv/commit/6c1833cc0fef64483fd54708add26fbbc8281afb))
* remove markdown package and ensure safe rendering of job achievements ([122523a](https://github.com/crackedngineer/codeurcv/commit/122523a855173ae535cf33ca392956ffa44ed99d))
* remove markdown2 dependency and implement pandoc for markdown to LaTeX conversion ([ebf8f45](https://github.com/crackedngineer/codeurcv/commit/ebf8f45391bcb5aa4b885babca75ecb3201cb24a))
* remove outdated achievement from current role at Mott MacDonald ([7edf799](https://github.com/crackedngineer/codeurcv/commit/7edf799a0fcfcc486cc8c83d3976ac763d7869ac))
* remove outdated achievement from work experience at Fynd ([d981c5b](https://github.com/crackedngineer/codeurcv/commit/d981c5bbb8d78713f0b7d3207856419bf00c622b))
* remove quotes from working-directory in GitHub Actions workflow ([3b87a6d](https://github.com/crackedngineer/codeurcv/commit/3b87a6da103d8aa3d143c2e50de2fc8f74230f24))
* remove unnecessary import of asyncio subprocess in render.py ([a48bc37](https://github.com/crackedngineer/codeurcv/commit/a48bc377bb1df79d307bbf39df990f301e6bd64b))
* remove unnecessary Pandoc feature from devcontainer configuration ([d8c0825](https://github.com/crackedngineer/codeurcv/commit/d8c08259d49b41ccd887c8e65c15d0fc7f156407))
* replace resumeSubItemWithDescription with resumeSubSubheading for project items ([35373bd](https://github.com/crackedngineer/codeurcv/commit/35373bdc7db9d173167b463d823d545f78e9757a))
* set working directory for LaTeX compilation step in GitHub Actions ([70e5be4](https://github.com/crackedngineer/codeurcv/commit/70e5be482194b0794847e4aeb2e4acd6cf6bcda1))
* specify output files for commit in PDF build workflow ([f5da2f7](https://github.com/crackedngineer/codeurcv/commit/f5da2f75560930645d463a42b9d9a2b07d270554))
* streamline LaTeX compile process and update resume summary ([2076590](https://github.com/crackedngineer/codeurcv/commit/20765905eb2e04590bd5673ac54034b67ec2a735))
* swap input parameters for LaTeX compilation step in GitHub Actions ([a04ef94](https://github.com/crackedngineer/codeurcv/commit/a04ef941d2ec0d1a5c8896dd0123be239c445af3))
* update action used in GitHub Actions workflow for CV building ([cdbb0aa](https://github.com/crackedngineer/codeurcv/commit/cdbb0aa8fcd4289d63a6948994c182e0f852580e))
* update author name in LaTeX template ([cbcd4ce](https://github.com/crackedngineer/codeurcv/commit/cbcd4cea9f5d82f04f41f2708a9c5dba4e660bd7))
* update build script to use correct config file extension and improve LaTeX compilation step ([f79ca2b](https://github.com/crackedngineer/codeurcv/commit/f79ca2b5a329ef33aa7d09d261d93f3ff5820efb))
* update degree format in education section and improve project listing layout ([dc74270](https://github.com/crackedngineer/codeurcv/commit/dc742701f5f9d5d509fde2464b0320fdff03e299))
* update fetch_template function to use BASE_DIR for template path resolution ([1fbf436](https://github.com/crackedngineer/codeurcv/commit/1fbf4360d77efa60931c891b9d7657d41b20cbfb))
* update git add commands to include all .tex and .pdf files in output directory ([99374ed](https://github.com/crackedngineer/codeurcv/commit/99374eddb0304f6f7d0f725fb8d2f00ff2b8c4fb))
* update GitHub token reference in release-please configuration ([8ab922f](https://github.com/crackedngineer/codeurcv/commit/8ab922f6eaf0d31d01a14d33b47546dd80167e57))
* update GPA and enhance job achievements with detailed descriptions and technologies ([cc0a1bf](https://github.com/crackedngineer/codeurcv/commit/cc0a1bf01661bc1c1c448b613ddee344c9df938f))
* update hyperlink formatting for website in LaTeX resume template ([858bd6a](https://github.com/crackedngineer/codeurcv/commit/858bd6ae183e2b0ecda2a4b9cbc8b411f94cc95b))
* update output file path for LaTeX resume and adjust formatting in template ([38a040a](https://github.com/crackedngineer/codeurcv/commit/38a040adf24e65a3301c8538e9239f14b441f3e0))
* update paths for PDF generation and output handling ([5ac2518](https://github.com/crackedngineer/codeurcv/commit/5ac251800a8567bf476faf863520d8771137e105))
* update pdfLaTeX installation to include additional LaTeX packages ([df87811](https://github.com/crackedngineer/codeurcv/commit/df87811fe3c7e117ab415dd0e9a20bc9ce9e73d3))
* update permissions to allow write access for contents in build workflow ([015e3ff](https://github.com/crackedngineer/codeurcv/commit/015e3ff3b4580b08bcbbc692eede44cb03c7ad38))
* update project listing format to include links and improve readability ([a593ec4](https://github.com/crackedngineer/codeurcv/commit/a593ec4f974d6210b428257f88192b3427c4dc79))
* update Python dependencies and enhance achievement formatting in resume ([dc92e57](https://github.com/crackedngineer/codeurcv/commit/dc92e5746bcfc3c2c5202d21f338657c5f023dc5))
* update render command in build script to use shorthand flag for config file ([fc60fef](https://github.com/crackedngineer/codeurcv/commit/fc60fefdf874aa9ff39eb18a177a73042db6c622))
* update resume item commands for improved formatting and readability ([a82b920](https://github.com/crackedngineer/codeurcv/commit/a82b920523544e3f83bd4b5d9195d864acec5402))
* update resume item commands for improved structure and readability ([19957fb](https://github.com/crackedngineer/codeurcv/commit/19957fbb8d88e56686b8d4ab8c6731d9cb54baf1))
* update resume item formatting to ensure proper rendering of achievements ([be16f88](https://github.com/crackedngineer/codeurcv/commit/be16f885c6f0065fa668952c7017183be6fa74b5))
* update resume template and rendering logic for improved structure and readability ([7ad0c78](https://github.com/crackedngineer/codeurcv/commit/7ad0c78f1ee866d44bca012d8c1b58f95e944ad4))
* update resume template and structure for improved readability and ATS compatibility ([5f71a1f](https://github.com/crackedngineer/codeurcv/commit/5f71a1f99be1087196c5a76b74263e88e39d5d67))
* update resume template syntax for improved compatibility and readability ([0027a7c](https://github.com/crackedngineer/codeurcv/commit/0027a7cc5c8444c871460a6ace59fdad246058df))
* update template path resolution to use BASE_DIR and TEMPLATES_DIR ([e70fbdb](https://github.com/crackedngineer/codeurcv/commit/e70fbdb01b147a583767df1e520647d361189d57))
* update work experience section to reflect current role and company ([bf961bb](https://github.com/crackedngineer/codeurcv/commit/bf961bbb9f9e4837e224a95c8e1675fd2e7c5cbb))
