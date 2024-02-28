   with open(str(DATA_DIR) # save it on the new version folder
                            + '/Settings.cfg', 'w') as configfile:
                        configparser.write(configfile)
                    
                    pretty_print(Style.RESET_ALL + get_string('config_saved'), 
                                 "success", "sys0")
                except Exception as e:
                    pretty_print(f"Error saving configfile: {e}" + str(e), 
                                 "error", "sys0")
                    pretty_print("Config won't be carried to the next version",
                        
                                 "warning", "sys0")

                if not os.path.exists(Settings.TEMP_FOLDER): # Make the Temp folder
                    os.makedirs(Settings.TEMP_FOLDER) 

                "warning", "sys0")
                    with open(file_path, 'wb') as f: 
                        for chunk in r.iter_content(chunk_size=1024 * 8): # Download file in chunks
                            if chunk:
                                dl += len(chunk)
                                done = int(50 * dl / file_size)
                                dl_perc = str(int(100 * dl / file_size))

                                if running_script:
                                    done = int(12.5 * dl / file_size)
                                    dl_perc = str(int(22.5 * dl / file_size))
  if discord_presence == "y":
        try:
            init_rich_presence()
        except Exception as e:
            debug_output(f'Error launching Discord RPC thread: {e}')
