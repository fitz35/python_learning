{
  description = "Impure Python environment flake";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
  

  outputs = { self, nixpkgs }:
    let
    
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python310Packages;

      impurePythonEnv = pkgs.mkShell rec {
        name = "impurePythonEnv";
        venvDir = "./.venv";
        buildInputs = [
         

          # python env
          pythonPackages.python
          pythonPackages.venvShellHook
          pkgs.autoPatchelfHook
          
          # python packages

          pythonPackages.python-dotenv
          pythonPackages.requests
          pythonPackages.psycopg2

          pythonPackages.tqdm

          # dependances

         
        ];


        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r requirements.txt
          autoPatchelf ./venv
        '';

        postShellHook = ''
          unset SOURCE_DATE_EPOCH
        '';

      };

    in {
      # Expose the environment as a default package
      defaultPackage.x86_64-linux = impurePythonEnv;
      # Expose the environment as a default shell
      devShells.x86_64-linux.default = impurePythonEnv;
    };
}