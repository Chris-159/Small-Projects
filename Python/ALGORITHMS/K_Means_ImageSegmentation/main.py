import basics as bs
import k_means

image_ = bs.image_get("test_img1.jpeg")

if image_.any():
    #content_histogram_ = bs.create_histogram(image_)
    clusters_res, centroids_res = k_means.start(image_, K=3)
    print(f'\nFinal cluster: {clusters_res}\nFinal centroids: {centroids_res}')

    colored_image = k_means.color_clusters(image_, clusters_res, centroids_res)
    bs.show_image(colored_image, title="Colored Image")

    save = input("\nDo you want to save the image? (y or n) ")
    while save not in ["y", "n"]:
        save = input("Please enter 'y' or 'n': ")
    
    if save == "y":
        bs.image_save(colored_image)
    elif save == "n":
        print("Exiting...")

else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
